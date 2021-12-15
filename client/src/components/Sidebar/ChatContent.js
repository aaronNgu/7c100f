import React from "react";
import { Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
  root: {
    display: "flex",
    justifyContent: "space-between",
    marginLeft: 20,
    flexGrow: 1,
  },
  username: {
    fontWeight: "bold",
    letterSpacing: -0.2,
  },
  previewText: {
    fontSize: 12,
    fontWeight: (props) => props.fontWeight,
    color: (props) => props.color,
    letterSpacing: -0.17,
  },
}));

const ChatContent = (props) => {
  const { conversation } = props;
  const { latestMessageText, otherUser, unreadMessageCount } = conversation;
  const hasUnreadMessages = unreadMessageCount > 0;

  const previewTextStyle = hasUnreadMessages ? 
                            {fontWeight: "bold", color: "#000000"} : 
                            {fontWeight: "normal", color: "#9CADC8"};
  const classes = useStyles(previewTextStyle);

  return (
    <Box className={classes.root}>
      <Box>
        <Typography className={classes.username}>
          {otherUser.username}
        </Typography>
        <Typography className={classes.previewText}>
          {latestMessageText}
        </Typography>
      </Box>
    </Box>
  );
};

export default ChatContent;
