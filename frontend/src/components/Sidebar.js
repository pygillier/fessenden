import React from 'react';
import { Box, Text } from "grommet";
import { RouterAnchor } from './routing.js';

const Sidebar = () => {
    return (
        <Box
            gridArea="sidebar"
            background="dark-1"
            width="small"
        >
            <RouterAnchor key="Import" path="/import">
                <Box pad={{ horizontal: "medium", vertical: "small" }}>
                    <Text>Import a feed</Text>
                </Box>
            </RouterAnchor>
            <RouterAnchor key="feeds" path="/feeds">
                <Box pad={{ horizontal: "medium", vertical: "small" }}>
                    <Text>All feeds</Text>
                </Box>
            </RouterAnchor>
        </Box>
    );
}

export default Sidebar;
