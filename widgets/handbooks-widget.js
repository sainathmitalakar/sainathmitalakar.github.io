// handbooks-widget.js

const handbooks = [
  { title: "Terraform Handbook", url: "handbooks/terraform.pdf" },
  { title: "Agentic AI Handbook", url: "handbooks/agentic-ai.pdf" }
];

function loadHandbooks() {
  const container = document.getElementById("handbooks-widget-container");
  if (!container) return;
  
  const section = document.createElement("section");
  section.id = "handbooks-widget";
  section.innerHTML = "<h2>Download Handbooks</h2><ul id='handbook-list'></ul>";
  
  container.appendChild(section);
  
  const list = section.querySelector("#handbook-list");
  handbooks.forEach(h => {
    const li = document.createElement("li");
    li.innerHTML = `<a href="${h.url}" download>${h.title}</a>`;
    list.appendChild(li);
  });
}

document.addEventListener("DOMContentLoaded", loadHandbooks);
