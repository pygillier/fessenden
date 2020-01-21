import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Typography from '@material-ui/core/Typography';
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import FeedList from './components/FeedList';
import ImportFeed from './components/ImportFeed';
import ApolloClient from 'apollo-boost';
import { ApolloProvider } from '@apollo/react-hooks';

const client = new ApolloClient();


const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
  },
  content: {
    flexGrow: 1,
    padding: theme.spacing(3),
  },
  toolbar: theme.mixins.toolbar,
}));

export default function App(props) {
  const classes = useStyles();
  const { container } = props;

  const [mobileOpen, setMobileOpen] = React.useState(false);

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen);
  };

  return (
    <ApolloProvider client={client}>
      <div className={classes.root}>
        <CssBaseline />
        <Router>
          <Header handleDrawerToggle={handleDrawerToggle}/>
          <Sidebar
            container={container}
            handleDrawerToggle={handleDrawerToggle}
            mobileOpen={mobileOpen} />

          <main className={classes.content}>
            <div className={classes.toolbar} />
            <Switch>
              <Route path="/import" component={ImportFeed} />
              <Route path="/feeds" component={FeedList} />
              <Route path="/feed/:slug">
                <Typography paragraph>
                  Feed details
                </Typography>
              </Route>
              <Route path="/">
                <Typography paragraph>
                  Main content
                </Typography>
              </Route>
            </Switch>
          </main>
        </Router>
      </div>
    </ApolloProvider>
  );
}
