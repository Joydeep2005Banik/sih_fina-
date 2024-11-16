document.addEventListener('DOMContentLoaded', () => {
    // Grabbing elements from the DOM (chat box, input field, buttons, etc.)
    const chatBox = document.getElementById('chatBox');
    const userInput = document.getElementById('userInput');
    const sendButton = document.getElementById('sendButton');
    const darkModeToggle = document.getElementById('darkModeToggle');
    const darkModeToggleNight = document.getElementById('darkModeToggleNight');

    // Function to append a new message (from user or bot) to the chat
    function appendMessage(sender, message) {
        const messageDiv = document.createElement('div');
        // Assign class based on sender and whether dark mode is active
        messageDiv.className = `${sender} message ${document.body.classList.contains('dark-mode') ? 'dark-mode' : ''}`;
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        // Auto-scroll chat box to the latest message
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // Function to send the user's message to the bot and get a response
    async function getBotResponse(userMessage) {
        try {
            // Sending a POST request with the user's message
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage }) // Convert message to JSON format
            });

            const data = await response.json(); // Parse the JSON response
            return data.response; // Return the bot's response
        } catch (error) {
            console.error('Error:', error);
            return 'Sorry, there was an error processing your request.'; // Error message for failed requests
        }
    }

    // Function to handle sending the user's message
    function handleSendMessage() {
        const userMessage = userInput.value.trim(); // Trim the input value to remove extra spaces
        if (userMessage) { // Check if the user has entered a message
            appendMessage('user', userMessage); // Append user's message to chat
            getBotResponse(userMessage).then(botResponse => {
                appendMessage('bot', botResponse); // Append bot's response to chat
            });
            userInput.value = ''; // Clear input field after sending the message
        }
    }

    // Function to toggle between light and dark mode
    function toggleDarkMode() {
        document.body.classList.toggle('dark-mode'); // Toggle dark mode class on body
        updateElementsForDarkMode(); // Update other elements for dark mode
    }

    // Function to update various elements when dark mode is toggled
    function updateElementsForDarkMode() {
        const elementsToUpdate = [
            document.querySelector('header'),
            document.querySelector('.chat-container'),
            document.querySelector('.chat-box'),
            document.querySelector('input[type="text"]'),
            sendButton
        ];

        const isDarkMode = document.body.classList.contains('dark-mode'); // Check if dark mode is active
        // Toggle dark mode class on each element that needs to be updated
        elementsToUpdate.forEach(element => element.classList.toggle('dark-mode', isDarkMode));
        // Toggle visibility of dark mode toggle icons
        darkModeToggle.classList.toggle('hidden', isDarkMode);
        darkModeToggleNight.classList.toggle('hidden', !isDarkMode);
    }

    // Event listener for the send button (click event)
    sendButton.addEventListener('click', handleSendMessage);

    // Event listener for the 'Enter' keypress in the input field
    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') { // Check if the pressed key is Enter
            handleSendMessage();
        }
    });

    // Event listeners for dark mode toggle buttons
    darkModeToggle.addEventListener('click', toggleDarkMode);
    darkModeToggleNight.addEventListener('click', toggleDarkMode);
});
