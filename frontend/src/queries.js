import { gql } from 'apollo-boost';

export const ALL_FEEDS = gql`
{
    allFeeds {
        edges {
            node {
                id
                title
                cover
            }
        }
    }
}
`;

export const DELETE_FEED = gql`
mutation DeleteFeed($id:ID!) {
    deleteFeed(id:$id){
        ok
    }
}
`;
