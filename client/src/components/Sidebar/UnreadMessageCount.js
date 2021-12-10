import React from 'react';
import { Box, Typography } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    root: {
      borderRadius: '50%',
      backgroundColor: "#3F92FF",
      padding: "3px 7px",
      flexGrow: 1,
      marginRight: 20,
    },
    count: {
        color: "#FFFFFF",
        fontSize: 10,
        fontWeight: 700,
    },
}));

const UnreadMessageCount = (props) => {
    const classes = useStyles();

    const { unreadMessageCount } = props;
    const  hasUnreadMessages = unreadMessageCount > 0;
    
    return (
        hasUnreadMessages &&
        <Box className={classes.root}>
            <Typography className={classes.count}>
                {unreadMessageCount}
            </Typography>
        </Box>
    );
}

export default UnreadMessageCount 
