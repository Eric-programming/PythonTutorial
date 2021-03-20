import { Component } from '@angular/core';
import { Node } from './helper/Node';
import { Transfer } from './helper/Transfer';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  tree: Node;
  constructor() {
    const transfer = new Transfer();
    this.tree = transfer.deserialize('1|2|NA|NA|3|4|5');
  }
  setTree(node: Node) {
    this.tree = node;
  }
}
