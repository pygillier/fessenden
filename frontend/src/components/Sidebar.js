import React from 'react';
import { makeStyles, useTheme } from '@material-ui/core/styles';
import Drawer from '@material-ui/core/Drawer';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import HomeIcon from '@material-ui/icons/Home';
import StorageIcon from '@material-ui/icons/Storage';
import AccountTreeIcon from '@material-ui/icons/AccountTree';
import FolderSpecialIcon from '@material-ui/icons/FolderSpecial';
import Hidden from '@material-ui/core/Hidden';
import { Link } from 'react-router-dom';

const drawerWidth = 240;

const useStyles = makeStyles(theme => ({
  drawer: {
    [theme.breakpoints.up('sm')]: {
      width: drawerWidth,
      flexShrink: 0,
    },
  },
  drawerPaper: {
    width: drawerWidth,
  },
  toolbar: theme.mixins.toolbar,
}));

const ListItemLink = (props) => <ListItem button component="a" {...props} />;
const ListItemRouter = (props) => <ListItem button component={Link} {...props} />;

const Sidebar = (props) => {
  const classes = useStyles();
  const theme = useTheme();

  const drawer = (
    <div>
      <List>
        <ListItemRouter to="/">
          <ListItemIcon><HomeIcon /></ListItemIcon>
          <ListItemText primary="Homepage" />
        </ListItemRouter>
        <ListItemRouter to="/feeds">
          <ListItemIcon><HomeIcon /></ListItemIcon>
          <ListItemText primary="All feeds" />
        </ListItemRouter>
        <ListItemRouter to="/import">
          <ListItemIcon><HomeIcon /></ListItemIcon>
          <ListItemText primary="Import a feed" />
        </ListItemRouter>
      </List>
      {process.env.NODE_ENV === 'development' &&
        <>
        <Divider />
        <List>
          <ListItemLink href="http://127.0.0.1:8000/graphql" target="_blank">
            <ListItemIcon><AccountTreeIcon /></ListItemIcon>
            <ListItemText primary="GraphQL console"/>
          </ListItemLink>
          <ListItemLink href="http://127.0.0.1:9000" target="_blank">
            <ListItemIcon><FolderSpecialIcon /></ListItemIcon>
            <ListItemText primary="MinIO dashboard"/>
          </ListItemLink>
          <ListItemLink href="http://127.0.0.1:8080" target="_blank">
            <ListItemIcon><StorageIcon /></ListItemIcon>
            <ListItemText primary="PG admin"/>
          </ListItemLink>
        </List>
        </>
      }
    </div>
  );

    return (
      <nav>
        <Hidden smUp implementation="css">
        <Drawer
            container={props.container}
            variant="temporary"
            anchor={theme.direction === 'rtl' ? 'right' : 'left'}
            open={props.mobileOpen}
            onClose={props.handleDrawerToggle}
            classes={{
              paper: classes.drawerPaper,
            }}
            ModalProps={{
              keepMounted: true, // Better open performance on mobile.
            }}
          >
        <div className={classes.toolbar} />
        {drawer}
      </Drawer>
      </Hidden>
      <Hidden xsDown implementation="css">
        <Drawer
          container={props.container}
        className={classes.drawer}
        variant="permanent"
        classes={{
          paper: classes.drawerPaper,
        }}
      >
        <div className={classes.toolbar} />
        {drawer}
      </Drawer>
      </Hidden>
      </nav>
    );
}

export default Sidebar;
