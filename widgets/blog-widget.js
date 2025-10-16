// blog-widget.js

const blogs = [
  {
    title: "RAG DevOps Assistant – AI-Powered Documentation Tool",
    date: "October 16, 2025",
    excerpt: "Learn how to leverage RAG for AI-powered documentation queries in DevOps...",
    url: "blogs/2025-10-16-rag-devops-assistant.html"
  },
  {
    title: "Terraform Horror Story",
    date: "October 12, 2025",
    excerpt: "A deep dive into misconfigurations and lessons learned in Terraform deployments...",
    url: "blogs/2025-10-12-terraform-horror-story.html"
  }
];

function loadBlogs() {
  const container = document.getElementById("blog-widget-container");
  if (!container) return;
  
  const section = document.createElement("section");
  section.id = "blog-widget";
  section.innerHTML = `<h2>Latest Blogs</h2><div id="blog-list"></div><a href="blogs.html">View All Blogs</a>`;
  
  container.appendChild(section);
  
  const blogList = section.querySelector("#blog-list");
  blogs.forEach(blog => {
    const div = document.createElement("div");
    div.className = "blog-item";
    div.innerHTML = `
      <h3>${blog.title}</h3>
      <p class="date">${blog.date}</p>
      <p class="excerpt">${blog.excerpt}</p>
      <a href="${blog.url}">Read More</a>
    `;
    blogList.appendChild(div);
  });
}

document.addEventListener("DOMContentLoaded", loadBlogs);
