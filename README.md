# spotify-canvases

Video URLs from [Spotify Canvas](https://canvas.spotify.com/en-us)

Note that these are obtained manually, as the links of the Canvases are random hashes. They do not relate to the track ID or anything in the [Get a Track endpoint](https://developer.spotify.com/documentation/web-api/reference/tracks/get-track/).

## How to get the Canvases

To get the Canvas of a song, you need to find out the request the Spotify mobile app is making by intercepting the network traffic from your mobile device.

Spotify Canvases are from `https://canvaz.scdn.co`.

On iOS, we use an app called [Charles Proxy](https://apps.apple.com/us/app/charles-proxy/id1134218562). They also have a [trial version available for desktop](https://www.charlesproxy.com/), where you can make your computer act as a proxy for your device. There are other programs that do this too, but just make sure that whatever program you're using has the ability to intercept HTTPs/SSL traffic.

## Contributing

If you would like to add some Spotify Canvas links, please submit a pull request. You could either edit the `canvases.json` file on GitHub, or clone this repository. We have made a Python 3 script that lets you easily add to the file. The only module you need installed is `requests`. This validates and gets the title and artist from the URI. **We will only accept pull requests with video URLs from `canvaz.scdn.co`**. We will not accept third-party links.
