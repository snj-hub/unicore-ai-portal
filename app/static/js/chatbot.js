const toggleBtn = document.getElementById("chat-toggle");
const widget = document.getElementById("chat-widget");
const form = document.getElementById("chat-form");
const input = document.getElementById("chat-input");
const messages = document.getElementById("chat-messages");

function appendMessage(sender, text) {
  const bubble = document.createElement("div");
  bubble.className = `bubble ${sender}`;
  bubble.textContent = text;
  messages.appendChild(bubble);
  messages.scrollTop = messages.scrollHeight;
}

async function sendMessage(message) {
  appendMessage("user", message);
  appendMessage("bot", "Typing...");

  const response = await fetch("/api/bot/message", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  messages.lastChild.remove();
  appendMessage("bot", data.reply);
}

toggleBtn?.addEventListener("click", () => {
  widget.classList.toggle("hidden");
  if (!messages.hasChildNodes()) {
    appendMessage("bot", "Hello! I am VCSM Bot. Ask me about your timetable or periods.");
  }
});

form?.addEventListener("submit", async (event) => {
  event.preventDefault();
  const message = input.value.trim();
  if (!message) return;

  input.value = "";
  await sendMessage(message);
});
