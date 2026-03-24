const tools = [
    {
        name: "ChatGPT",
        desc: "AI chatbot for answers",
        link: "https://chat.openai.com"
    },
    {
        name: "Midjourney",
        desc: "AI image generator",
        link: "https://midjourney.com"
    },
    {
        name: "Runway ML",
        desc: "AI video editing",
        link: "https://runwayml.com"
    },
    {
        name: "Copy.ai",
        desc: "AI content writer",
        link: "https://copy.ai"
    }
];

const container = document.getElementById("tools-container");

function displayTools(list) {
    container.innerHTML = "";

    list.forEach(tool => {
        container.innerHTML += `
            <div class="tool-card">
                <h2>${tool.name}</h2>
                <p>${tool.desc}</p>
                <a href="${tool.link}" target="_blank">Visit</a>
            </div>
        `;
    });
}

displayTools(tools);

// 🔍 search feature
document.getElementById("search").addEventListener("input", function() {
    const value = this.value.toLowerCase();

    const filtered = tools.filter(tool =>
        tool.name.toLowerCase().includes(value)
    );

    displayTools(filtered);
});