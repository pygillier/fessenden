import React from 'react';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Grommet, Box, Grid, Text } from "grommet";
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import FeedList from './components/FeedList';
import ImportFeed from './components/ImportFeed';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';

const client = new ApolloClient();

const theme = {
  global: {
    font: {
      family: 'Open Sans',
    },
  },
  heading: {
    font: {
      family: "Raleway",
    }
  }
};

const App = () => {

  return (
    <ApolloProvider client={client}>
      <Grommet full theme={theme}>
        <Grid
          fill
          rows={["auto", "flex"]}
          columns={["auto", "flex"]}
          areas={[
            { name: "header", start: [0, 0], end: [1, 0] },
            { name: "sidebar", start: [0, 1], end: [0, 1] },
            { name: "main", start: [1, 1], end: [1, 1] }
          ]}
        >
          <Router>
            <Header/>
            <Sidebar/>
            <Switch>
              <Route path="/import" component={ImportFeed} />
              <Route path="/feeds" component={FeedList} />
              <Route path="/feed/:slug">
                <Box gridArea="main" justify="center" align="center">
                  <Text>Feed details</Text>
                </Box>
              </Route>
              <Route path="/">
                <Box gridArea="main" justify="center" align="center">
                  <Text>home</Text>
                </Box>
              </Route>
            </Switch>
          </Router>
        </Grid>
      </Grommet>
    </ApolloProvider>
  );
}

export default App;
