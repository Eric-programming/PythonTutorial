import { Component, HostListener, Input } from '@angular/core';
import { Node } from '../helper/Node';
import { UUID } from 'angular2-uuid';
import { TreeService } from '../service/tree.service';

@Component({
  selector: 'app-node',
  templateUrl: './node.component.html',
  styleUrls: ['./node.component.css'],
})
export class NodeComponent {
  @Input() currentNode: Node;
  constructor(private ts: TreeService) {}
  isSelected: boolean = false;
  addNode() {
    this.ts.addNode(this.currentNode);
  }
  selectNode = () => (this.isSelected = !this.isSelected);
  editVal() {
    const val = prompt("Edit Node's val", this.currentNode.val);
    if (!val) return;
    this.ts.editNode(this.currentNode, val);
  }
  deleteNode() {
    this.ts.deleteNode(this.currentNode);
  }
  @HostListener('window:keyup', ['$event'])
  keyEvent(event: KeyboardEvent) {
    if (!this.isSelected) return;
    if (
      event.code != 'Enter' &&
      event.code != 'Backquote' &&
      event.code !== 'Backspace'
    )
      return;
    if (event.code === 'Enter') {
      this.addNode();
    }
    if (event.code === 'Backquote') {
      this.editVal();
    }
    if (event.code === 'Backspace') {
      console.log('Backspace');
      this.deleteNode();
    }
    this.isSelected = false;
  }
}
