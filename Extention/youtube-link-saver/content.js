chrome.action.onClicked.addListener((tab) => {
  if (tab.url.includes("youtube.com/watch")) {
    const videoUrl = tab.url;

    // Set cookie
    chrome.cookies.set({
      url: "https://www.youtube.com",
      name: "saved_video",
      value: encodeURIComponent(videoUrl),
      expirationDate: Math.floor(Date.now() / 1000) + 3600 * 24 * 7  // 7 days
    }, function (cookie) {
      console.log("Cookie set:", cookie);
    });
  }
});
