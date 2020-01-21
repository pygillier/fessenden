
import React from 'react';
import { Box, Menu, Heading } from "grommet";
import { Link } from 'react-router-dom';

const Header = () => {
    return (
        <Box
          gridArea="header"
          direction="row"
          align="center"
          justify="between"
          pad={{ horizontal: "medium", vertical: "small" }}
          background="dark-1"
        >
          <Heading as={Link} to="/" level="1" size="small">Fessenden</Heading>
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
