async function download() {
  const url = document.getElementById("url").value;
  const format = document.getElementById("format").value;

  if (!url) {
    alert("Please enter URL");
    return;
  }

  document.getElementById("status").innerText = "Downloading...";

  const res = await fetch("/api/download", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url, format }),
  });

  if (res.ok) {
    const blob = await res.blob();
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "video";
    link.click();
    document.getElementById("status").innerText = "Done!";
  } else {
    document.getElementById("status").innerText = "Failed: " + res.statusText;
  }
}
