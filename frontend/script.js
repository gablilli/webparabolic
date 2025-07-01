async function download() {
  const url = document.getElementById("url").value;
  const format = document.getElementById("format").value;
  const token = grecaptcha.getResponse();
  if (!url || !token) return alert("Please enter URL and complete CAPTCHA");

  document.getElementById("status").innerText = "Downloading...";

  const res = await fetch("/api/download", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ url, format, token })
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
  grecaptcha.reset();
}
