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
