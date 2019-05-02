

import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    todos: []
  };

  componentDidMount() {
    this.getTodos();
  }

  getTodos() {
    axios
      .get('http://127.0.0.1:8000/api/')
      .then(res => {
        this.setState({ todos: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        {this.state.todos.map(item => (
          <div key={item.id}>
            <h1>{item.songs}</h1>
            <h3>{item.mood}</h3>
            <ul>
            <li><span>{item.recommendation_one}</span></li>
            <li><span>{item.recommendation_two}</span></li>
            <li><span>{item.recommendation_three}</span></li>
            <li><span>{item.recommendation_four}</span></li>
            <li><span>{item.recommendation_five}</span></li>
            </ul>
          </div>
        ))}
      </div>
    );
  }
}

export default App;
