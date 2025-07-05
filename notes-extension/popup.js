document.getElementById("load-notes").addEventListener("click", async () => {
  const res = await fetch("http://127.0.0.1:5000/api/notes"); // You must expose this API
  const data = await res.json();

  const ul = document.getElementById("notes");
  ul.innerHTML = "";
  data.notes.forEach(note => {
    const li = document.createElement("li");
    li.innerText = note;
    ul.appendChild(li);
  });
});
