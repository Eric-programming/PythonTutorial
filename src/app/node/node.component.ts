import { Component, HostListener, Input, OnInit } from '@angular/core';
import { deleteNodeInTree } from '../helper/DeleteNode';
import { Node } from '../helper/Node';

@Component({
  selector: 'app-node',
  templateUrl: './node.component.html',
  styleUrls: ['./node.component.css'],
})
export class NodeComponent {
  @Input() currentNode: Node;
  @Input() parentNode: Node;

  isSelected: boolean = false;
  addNode() {
    if (this.currentNode.left == null) {
      this.currentNode.left = new Node('L');
    } else {
      this.currentNode.right = new Node('R');
    }
  }
  selectNode = () => (this.isSelected = !this.isSelected);
  editVal() {
    const val = this.currentNode.val;
    this.currentNode.val =
      prompt("Edit Node's val", this.currentNode.val) || val;
  }
  deleteNode() {
    this.currentNode = deleteNodeInTree(
      this.currentNode,
      this.parentNode,
      this.parentNode.left === this.currentNode
    );
  }
  @HostListener('window:keyup', ['$event'])
  keyEvent(event: KeyboardEvent) {
    console.log('event', event);
    if (!this.isSelected) return;
    if (
      event.code != 'Enter' &&
      event.code != 'Backquote' &&
      event.code !== 'Backspace'
    )
      return;
    console.log(this.currentNode.val);
    if (event.code === 'Enter') {
      this.addNode();
    }
    if (event.code === 'Backquote') {
      this.editVal();
    }
    if (event.code === 'Backspace') {
      this.deleteNode();
    }
    this.isSelected = false;
  }
}
