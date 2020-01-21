import { gql } from 'apollo-boost';

export const ALL_FEEDS = gql`
{
    allFeeds {
        edges {
            node {
                id
                title
                cover
                description
            }
        }
    }
}
`;

export const IMPORT_FEED = gql`
mutation ImportFeed($url:String!){
  importFeed(input:{
    feedUrl: $url
  }) {
    clientMutationId
    feed {
      id
      title
      cover
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
