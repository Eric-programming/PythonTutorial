import { Component, HostListener, Input, OnInit } from '@angular/core';
import { Node } from '../helper/Node';

@Component({
  selector: 'app-node',
  templateUrl: './node.component.html',
  styleUrls: ['./node.component.css'],
})
export class NodeComponent implements OnInit {
  @Input() currentNode: Node;
  constructor() {}
  ngOnInit(): void {}
  isSelected: boolean = false;
  addNode() {
    if (this.currentNode.left == null) {
      this.currentNode.left = new Node('L');
    } else {
      this.currentNode.right = new Node('R');
    }
  }
  selectNode() {
    this.isSelected = true;
  }

  @HostListener('window:keyup', ['$event'])
  keyEvent(event: KeyboardEvent) {
    if (!this.isSelected) return;
    if (event.code != 'Enter' && event.code != 'Backquote') return;
    console.log(this.currentNode.val);
    if (event.code === 'Enter') {
      console.log('Enter');
    }

    if (event.code === 'Backquote') {
      console.log('Backquote');
    }
    this.isSelected = false;
  }
}
