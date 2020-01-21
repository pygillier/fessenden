import React from 'react';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import { makeStyles } from '@material-ui/core/styles';
import { useMutation } from '@apollo/react-hooks';
import {IMPORT_FEED} from '../queries';

const useStyles = makeStyles(theme => ({
  root: {
    '& .MuiTextField-root': {
      margin: theme.spacing(1),
      width: 200,
    },
  },
}));

const ImportFeed = () => {
    const classes = useStyles();
    const [importFeed, { data, loading, error }] = useMutation(IMPORT_FEED);

    function submitUrl(e) {
        e.preventDefault();
        importFeed({ variables: { url: e.value.feed_url } });
    };



    console.log(data);

    return (
        <div>
        <form className={classes.root} noValidate autoComplete="off" onSubmit={submitUrl}>
            <TextField name="feed_url" label="Feed URL" required />
            <Button variant="contained" color="primary" type="submit">
                Primary
            </Button>
        </form>
        <ul>
            <li>http://feeds.feedburner.com/TheBunkerPodcast</li>
        </ul>
        </div>
    );
}

export default ImportFeed;
