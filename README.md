# Instagram Growth Hacker

Instagram Growth Hacker allows users to post content on their instagram account completely automated by taking content from other sites(specified sources by user). (Same like IFTTT.com) Example: Let's say I give a source url - https://www.reddit.com/r/programmerhumor/hot/.json The tool will check for new posts on this json from time to time and if it founds new post in this subreddit it will automatically post it on our instagram account.

## Key Callouts / Assumptions


## Use Cases

- Automatically find and publish new posts from given source
- Filter posts by various metrics (e.g. post type - image or video)
- Like posts on given hashtags
- Comment on posts based on given hashtags
- Interact with followers of a specified user (like/comment)
- Take a random post from already posted posts and publish it as a story
- Stats section to see the number of posts published, views, interactions for each campaign
- Campaign users can create multiple campaigns

## Requirements

### Functional Requirements

- Instagram login
- JSON Scrapper to scrap new posts from source
- Each campaign contain sources and insta account list
- Set maximum posts published per day per account
- Choose Post type: Select content (photo/video) from the given sources
- Users can provide hashtags and tool will randomly select hashtag from the subset when posting a new post


### Non-Functional Requirements

- SAAS product
- Two Subscriptions
    - One Campaign
    - Unlimited Campaigns
- Ability to add multiple type of sources (JSON/RSS)

## Authors

- Saurav Kumar
- Aakash Deep

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements