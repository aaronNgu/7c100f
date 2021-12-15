import React from 'react';
import { Box, Badge } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    root: {
      marginRight: 29,
    },
}));

const UnreadMessageCount = (props) => {
    const classes = useStyles();

    const { unreadMessageCount } = props;
    
    return (
        <Box className={classes.root}>
            <Badge badgeContent={unreadMessageCount} color="primary"/>
        </Box>
    );
}

export default UnreadMessageCount 
