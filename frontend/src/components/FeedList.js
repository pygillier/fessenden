import React from 'react';
import { Main, Heading } from "grommet";
import FeedCard from './FeedCard';
import { useQuery, useMutation } from '@apollo/react-hooks';
import {ALL_FEEDS, DELETE_FEED} from '../queries';

const FeedList = () => {

    const { data, loading, error } = useQuery(ALL_FEEDS);
    const [deleteFeed, {deleted}] = useMutation(DELETE_FEED);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error :(</p>;

    console.log(data)

    const feedList = data.allFeeds.edges.map((feed) =>
        <FeedCard key={feed.node.id} feed={feed.node} deleteFeed={deleteFeed}/>
    );


    return(
        <Main pad="medium">
            <Heading>All feeds</Heading>
            {feedList}

        </Main>
    );
}

export default FeedList;
