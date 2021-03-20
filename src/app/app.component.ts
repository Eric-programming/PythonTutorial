import { Component } from '@angular/core';
import { Node } from './helper/Node';
import { Transfer } from './helper/Transfer';
import { TreeService } from './service/tree.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent {
  tree: Node;
  constructor(private ts: TreeService) {
    const transfer = new Transfer();
    this.ts.setRoot(transfer.deserialize('1|2|NA|NA|3|4|5'));
    this.ts.getRoot().subscribe((res) => {
      this.tree = res;
    });
  }
  setTree(node: Node) {
    this.tree = node;
  }
}
