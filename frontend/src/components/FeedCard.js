import React from 'react'
import { Grommet, grommet, Box, Image, Heading, Button } from 'grommet';
import { Nodes, Trash } from 'grommet-icons'


const FeedCard = (props) => {

  function handleDelete() {
    props.deleteFeed({variables: {id: props.feed.id}});
  }

  return (
    <Grommet theme={grommet}>
      <Box direction="column" align="center" gap="xxsmall" pad="small" round="medium" border={{"size":"medium","side":"all","color":"accent-4"}} width="medium">
        <Image src="https://placekitten.com/200/300" fit="contain" />
        <Heading level="3">
          {props.feed.title}
        </Heading>
        <Box align="center" justify="between" direction="row" gap="xlarge" fill="horizontal">
          <Button path='/' label="All episodes" primary={true} reverse={false} icon={<Nodes />} />
          <Button label="Delete" icon={<Trash />} hoverIndicator={true} color="status-critical" onClick={handleDelete} />
        </Box>
      </Box>
    </Grommet>
  )
}

export default FeedCard;
