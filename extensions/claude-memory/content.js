const processedPairs = new Set();

let projectContext = null;

async function fetchProjectContext() {
    try {
        const response = await fetch("http://127.0.0.1:8000/memory/context");

        const data = await response.json();

        projectContext = data.context;

        if (!projectContext || projectContext.trim() === "") {
            console.log("No project memory found.");
            return;
        }

        console.log("========== PROJECT CONTEXT ==========");
        console.log(projectContext);
        console.log("=====================================");

        if (window.location.pathname === "/new") {
            createInsertButton();
        }

    } catch (error) {
        console.error("Failed to fetch project context:", error);
    }
}

function createInsertButton() {

    if (document.getElementById("ai-memory-button")) {
        return;
    }

    const button = document.createElement("button");

    button.id = "ai-memory-button";
    button.innerText = "Insert Memory";

    button.style.position = "fixed";
    button.style.bottom = "20px";
    button.style.right = "20px";
    button.style.zIndex = "999999";
    button.style.padding = "12px 18px";
    button.style.background = "#7c3aed";
    button.style.color = "white";
    button.style.border = "none";
    button.style.borderRadius = "10px";
    button.style.cursor = "pointer";
    button.style.fontSize = "14px";
    button.style.boxShadow = "0 4px 12px rgba(0,0,0,.25)";

    button.onclick = insertContext;

    document.body.appendChild(button);
}

function insertContext() {

    if (!projectContext) {
        return;
    }

    const editor = document.querySelector(
        '[data-testid="chat-input"]'
    );

    if (!editor) {
        alert("Claude editor not found.");
        return;
    }

    editor.focus();

    // Clear editor
    editor.innerHTML = "";

    // Insert plain text
    document.execCommand("insertText", false, projectContext);

    console.log("Memory inserted.");
}

async function sendConversation(user, assistant) {
    try {

        const response = await fetch("http://127.0.0.1:8000/memory/event", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                chat_id: window.location.pathname,
                timestamp: new Date().toISOString(),
                user_message: user,
                assistant_message: assistant,
                changed_files: [],
                git_diff: ""
            }),
        });

        const memory = await response.json();

        console.log("Memory updated:");
        console.log(memory);

    } catch (error) {
        console.error("Failed to send conversation:", error);
    }
}

function getUserMessages() {
    return [...document.querySelectorAll('[data-testid="user-message"]')]
        .map(el => el.innerText.trim())
        .filter(Boolean);
}

function getAssistantMessages() {
    return [...document.querySelectorAll('[data-is-streaming="false"] .standard-markdown')]
        .map(el => el.innerText.trim())
        .filter(Boolean);
}

function hashPair(user, assistant) {
    return `${user}\n---\n${assistant}`;
}

function processConversation() {

    const users = getUserMessages();
    const assistants = getAssistantMessages();

    const pairCount = Math.min(users.length, assistants.length);

    for (let i = 0; i < pairCount; i++) {

        const user = users[i];
        const assistant = assistants[i];

        const id = hashPair(user, assistant);

        if (processedPairs.has(id)) {
            continue;
        }

        processedPairs.add(id);

        console.log("========== NEW CONVERSATION ==========");
        console.log(user);
        console.log(assistant);

        sendConversation(user, assistant);
    }
}

const observer = new MutationObserver(() => {
    processConversation();
});

observer.observe(document.body, {
    childList: true,
    subtree: true,
});

console.log("AI Memory Agent started.");

if (window.location.pathname === "/new") {
    fetchProjectContext();
}

processConversation();