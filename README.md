<h1>Scraping Billboard 100</h1>
The Project enables you travel back in time to revisit the Top 100 Songs of any week/year of your choice. It uses Beautiful Soup to scrape data from this website and creates a Spotify playlist with this data so you can always remember the Good ol'days.<br>

<h2>Requirements</h2>
<ul>
  <li>Python 3.8 or higher.</li>
  <li>Install and import Beautiful Soup Library</li>
  <li>Create a Spotify account</li>
  <li>Spotipy API to manage the Spotify Account</li>
  <li>Set a redirect uri(just a fancy name for any url, it can be your localhost http://127.0.0.1 or http://example.com) as required by the Spotipy API</li>
  <li>Save your login details as well as your redirect uri</li>
</ul>
<hr>
<h3>What to do</h3>
<ol>
  <li>Fork this Git and clone to your local PC.</li>
  <li>Set your Spotify Login details by creating the environment variables to exactly match those stated in main.py</li>
  <li>Run the code and input the date(in this format: YYYY-MM-DD) you would like to get the top 100 songs.</li>
  <li>Populate the envirenment variables below with the correct values.</li>
  <ul>
    <li>CLIENT_ID=codeGivenWhenYouCreateSpotifyAccount</li>
    <li>CLIENT_SECRET=secretKeyGivenWhenYouCreateSpotifyAccount</li>
    <li>REDIRECT_URI=theWebsiteToRedirectToAsRequiredByTheSpotifyAPI</li>
  </ul>
  <li>That's all you need to do for now.</li>
</ol>
<hr>
<h3>Results</h3>
<img src="https://raw.githubusercontent.com/obiora789/Scraping_Billboard_100/obiora789-patch-1/List_of_Artists_and_Songs.jpg" alt="artistsAndSongsGenerated.jpg">
<img src="https://raw.githubusercontent.com/obiora789/Scraping_Billboard_100/obiora789-patch-1/Spotify_playlist_generated.jpg" alt="spotifyPlaylistGenerated.jpg">
<hr>
<h3>Bugs</h3>
<p>None as at the time of this documentation. 😉</p>

