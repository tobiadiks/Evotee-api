import React, { Component } from "react";

class Counter extends Component {
  state = {
    count: 0,
    counters: [
      { id: 1, value: 0 },
      { id: 2, value: 0 },
      { id: 3, value: 0 },
      { id: 3, value: 0 },
    ],
  };

  handleIncrement = () => {
    this.setState({ count: this.state.count + 1 });
  };
  render() {
    return (
      <React.Fragment>
        <ul>
          <span className={this.getBadgeColor()}>{this.formatCount()} </span>
          <button
            onClick={this.handleIncrement}
            className="btn btn-secondary btn-sm"
          >
            Increment
          </button>
        </ul>
      </React.Fragment>
    );
  }
  getBadgeColor() {
    let classes = "badge m-2 badge-";
    classes += this.state.count === 0 ? "warning" : "primary";
    return classes;
  }

  formatCount() {
    const { count } = this.state;
    return count === 0 ? "Zero" : count;
  }
}

export default Counter;
