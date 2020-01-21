import React from 'react';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import FeedCard from './FeedCard';
import { useQuery, useMutation } from '@apollo/react-hooks';
import {ALL_FEEDS, DELETE_FEED} from '../queries';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

const FeedList = () => {

    const classes = useStyles();
    const { data, loading, error } = useQuery(ALL_FEEDS);
    const [deleteFeed] = useMutation(DELETE_FEED);

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error :(</p>;

    const feedList = data.allFeeds.edges.map((feed) =>
        <Grid item xs={4}>
            <FeedCard key={feed.node.id} feed={feed.node} deleteFeed={deleteFeed}/>
        </Grid>
    );


    return(
        <div className={classes.root}>
            <Grid container spacing={3}>
                {feedList}
            </Grid>
        </div>
    );
}

export default FeedList;
