import React from 'react';
import { Box, Text } from "grommet";
import { Link } from 'react-router-dom';

const Sidebar = () => {
    return (
        <Box
            gridArea="sidebar"
            background="dark-3"
            width="small"
            animation={[
              { type: "fadeIn", duration: 300 },
              { type: "slideRight", size: "xlarge", duration: 150 }
            ]}
        >
            <Link render="Anchor" key="feeds" to="/feeds">
                <Box pad={{ horizontal: "medium", vertical: "small" }}>
                    <Text>All feeds</Text>
                </Box>
            </Link>
        </Box>
    );
}

export default Sidebar;
