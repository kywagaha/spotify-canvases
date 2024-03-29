# spotify-canvases

**Archived. Please check out [this project](https://github.com/itsmeow/Spicetify-Canvas) and [this project](https://github.com/bartleyg/my-spotify-canvas) for reverse engineered solutions for the Spotify Canvas API.**

Video URLs from [Spotify Canvas](https://canvas.spotify.com/en-us)

Note that these are obtained manually, as the links of the Canvases are random hashes. They do not relate to the track ID or anything in the [Get a Track endpoint](https://developer.spotify.com/documentation/web-api/reference/tracks/get-track/).

## How to get the Canvases

To get the Canvas of a song, you need to find out the request the Spotify mobile app is making by intercepting the network traffic of your mobile device.

Spotify Canvases are from `https://canvaz.scdn.co`.

On iOS, we use an app called [Charles Proxy](https://apps.apple.com/us/app/charles-proxy/id1134218562). They also have a [trial version available for desktop](https://www.charlesproxy.com/), where you can make your computer act as a proxy for your device. There are other programs that do this too, but just make sure that whatever program you're using has the ability to intercept HTTPs/SSL traffic.

## Contributing

If you would like to add some Spotify Canvas links, please submit a pull request. **We will only accept pull requests with video URLs from `canvaz.scdn.co`**. We will not accept third-party links. However, if you would like to submit a custom Canvas, like [these two](https://github.com/kywagaha/spotify-canvases/blob/2b8ef20f3efb5dfa5907b5bc984952aa5d54df89/canvases.json#L729-L740), we would gladly upload it to our own S3 and publish it here.
