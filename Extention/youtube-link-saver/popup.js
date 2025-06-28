document.getElementById("send-btn").addEventListener("click", () => {
  const input = document.getElementById("chat-input");
  const message = input.value.trim();

  if (message) {
    const msgDiv = document.createElement("div");
    msgDiv.textContent = "You: " + message;
    document.getElementById("messages").appendChild(msgDiv);
    input.value = "";

    // Optional: bot response
    setTimeout(() => {
      const botMsg = document.createElement("div");
      botMsg.textContent = "Bot: Got it!";
      document.getElementById("messages").appendChild(botMsg);
    }, 500);
  }
});
