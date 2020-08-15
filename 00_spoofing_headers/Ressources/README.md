# Spoofing headers

## Vulnerability 
* Run `sitemap` script showing available links in the landing page
* Click on `© BornToSec` at the bottom of the page which suspiciously direct to 
`/?page=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c`
* View page source which contains the following
```
<!--
You must cumming from : "https://www.nsa.gov/" to go to the next step
-->

<!--
Let's use this browser : "ft_bornToSec". It will help you a lot.
-->
```
* Request the page with modified request headers `Referer` (the
 address of the previous web page from which a link to the currently requested 
 page was followed) and `User-agent` (a string that lets
  servers and network peers identify the application) as specified
```
curl http://[host]/index.php\?page\=e43ad1fdc54babe674da7c7b8f0127bde61de3fbe01def7d00f151c2fcca6d1c \
-H "Referer: https://www.nsa.gov/" -H "User-Agent: ft_bornToSec" | grep flag
```

## Attack
* Providing publicly available hints in a source page can be used by an
 attacker.
* Testing several User-Agents can be used to test the website behaviour. Some 
websites react in different ways just based on the User-Agent passed by the 
browser.

## Fix
* Don't show business logic in code served by the server to the client
* Be cautious to not disclose sensitive information only based on the 
`User-Agent` or `Referer` request headers.

## References
https://isc.sans.edu/forums/diary/HTTP+Headers+the+Achilles+heel+of+many+applications/22382/
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
