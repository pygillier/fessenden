import * as React from "react";
import { RouteComponentProps, withRouter } from "react-router";

import { Anchor, AnchorProps, Button, ButtonProps } from "grommet";

interface RouterLinkProps {
  path: string;
}
const RouterAnchorBase = (props: RouteComponentProps & RouterLinkProps & AnchorProps) => {
  const anchorProps = props;
  return <Anchor {...anchorProps} onClick={() => props.history.push(props.path)} />;
};

const RouterAnchor = withRouter(RouterAnchorBase);

const RouterButtonBase = (props: RouteComponentProps & RouterLinkProps & ButtonProps) => {
  const buttonProps = props;
  return <Button {...buttonProps} onClick={() => props.history.push(props.path)} />;
};

const RouterButton = withRouter(RouterButtonBase);

export { RouterAnchor, RouterButton };
