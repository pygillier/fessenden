
import React from 'react';
import { Box, Button, Menu } from "grommet";
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <Box
          gridArea="header"
          direction="row"
          align="center"
          justify="between"
          pad={{ horizontal: "medium", vertical: "small" }}
          background="dark-2"
        >
            <Button>
                <Link size="large" to="/">Fessenden</Link>
            </Button>
            <Menu
                label="my@email"
                items={[
                    { label: 'My profile', onClick: () => {} },
                    { label: 'Logout', onClick: () => {} },
                ]}
            />
        </Box>
    );
}

export default Header;
