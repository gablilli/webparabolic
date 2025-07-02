<script>
  let url = '';
  let format = 'best';
  let status = '';
  
  async function download() {
    if (!url.trim()) {
      alert('Please enter a URL');
      return;
    }
    status = 'Downloading...';

    try {
      const res = await fetch('/api/download', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url, format })
      });
      if (!res.ok) {
        const err = await res.json();
        status = 'Error: ' + (err.detail || res.statusText);
        return;
      }
      const blob = await res.blob();
      const filename = res.headers.get('content-disposition')?.split('filename=')[1] || 'video';

      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.download = filename.replace(/["']/g, '');
      document.body.appendChild(link);
      link.click();
      link.remove();

      status = 'Download complete!';
    } catch(e) {
      status = 'Download failed: ' + e.message;
    }
  }
</script>

<style>
  :global(body) {
    background-color: #121212;
    color: #eee;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
  }
  .container {
    background: #1f1f1f;
    padding: 2rem;
    border-radius: 12px;
    width: 350px;
    box-shadow: 0 0 15px #0b84f6;
    text-align: center;
  }
  input, select, button {
    width: 100%;
    padding: 0.7rem;
    margin-top: 1rem;
    border-radius: 8px;
    border: none;
    font-size: 1rem;
  }
  button {
    background: #0b84f6;
    color: white;
    cursor: pointer;
  }
  button:hover {
    background: #0a72d7;
  }
  #status {
    margin-top: 1rem;
    min-height: 1.4rem;
  }
</style>

<div class="container">
  <h1>YT Downloader</h1>
  <input placeholder="Enter YouTube URL" bind:value={url} />
  <select bind:value={format}>
    <option value="best">Best quality</option>
    <option value="bestaudio">Audio only</option>
  </select>
  <button on:click={download}>Download</button>
  <div id="status">{status}</div>
</div>
