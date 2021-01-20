import Button from "@material-ui/core/Button";
import Card from "@material-ui/core/Card";
import Typography from "@material-ui/core/Typography";
import axios from "axios";
import React, { Component } from "react";

class Voters extends Component {
  constructor() {
    super();
    this.state = {
      data: [],
    };
  }

  fetchData() {
    // fetch (`http://localhost:8000/api/contestant-detail/232198962`)
    // .then(response => response.json())
    // .then((data)=>{
    //     this.setState({
    //         data:data
    //     });
    //     console.log(data);
    // });
    // PUT REQUEST SUCCESSFUL
    axios.put(
      `http://localhost:8000/api/contestant-update/506105851/`, //PUT request
      {
        contestantName: "Ayo Bamakonatyiii",
        position: "vice President",
        votes: 750,
        electionName: 456237882,
        is_active: true,
        contestantId: 506105851,
      },
      {
        headers: {
          Accept: "application/json",
          "Content-type": "application/json",
        },
      }
    );
  }

  componentDidMount() {
    this.fetchData();
  }

  render() {
    const voter = this.state.data;
    //  const row = voter.map((emp)=>
    // <><li>
    //       Name : {emp.contestantName}
    //   </li>
    //    <li>Position: {emp.position}</li>
    //     <li>Votes: {emp.votes}</li>
    //    <li>electionId: {emp.electionName}</li>
    //    <p></p>
    //    </>)
    return (
      <div>
        {/*row*/}
        <Card
          variant="elevation"
          style={{
            backgroundColor: "blueviolet",
            width: "20%",
            alignItems: "center",
            color: "white",
          }}
        >
          NAME: *
          <Typography
            variant="h4"
            style={{
              color: "white",
              fontFamily: "sans-serif",
              alignContent: "center",
            }}
          >
            {voter.contestantName}
          </Typography>
          POSITION: *
          <Typography
            variant="h5"
            style={{
              color: "white",
              fontFamily: "sans-serif",
            }}
          >
            {voter.position}
          </Typography>
          VOTES: *
          <Typography
            variant="h5"
            style={{
              color: "white",
              fontFamily: "sans-serif",
            }}
          >
            {voter.votes}
          </Typography>
          <Button
            variant="filled"
            style={{
              backgroundColor: "white",
            }}
          >
            Vote
          </Button>
        </Card>
      </div>
    );
  }
}

export default Voters;
