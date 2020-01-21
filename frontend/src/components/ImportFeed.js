import React from 'react';
import { useMutation } from '@apollo/react-hooks';
import { Main, Button, Heading, Form, FormField, Text } from "grommet";
import {IMPORT_FEED} from '../queries';

const ImportFeed = () => {

    const [importFeed, { data, loading, error }] = useMutation(IMPORT_FEED);

    function submitUrl(e) {
        importFeed({ variables: { url: e.value.feed_url } });
    };

    console.log(data);

    return (
        <Main pad="medium">
            <Heading level="2" margin="xsmall">Import a feed</Heading>
            <Form onSubmit={submitUrl}>
                <FormField name="feed_url" label="Feed URL" required placeholder="http://"/>
                <Button type="submit" primary label="Submit" />
            </Form>
            <ul>
            <li>http://feeds.feedburner.com/TheBunkerPodcast</li>
            </ul>
        </Main>
    );
}

export default ImportFeed;