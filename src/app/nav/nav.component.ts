import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { Node } from '../helper/Node';
import { Transfer } from '../helper/Transfer';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrls: ['./nav.component.css'],
})
export class NavComponent {
  @Input() cur: Node;
  @Output() emitNode = new EventEmitter<Node>();
  transfer: Transfer = new Transfer();
  encrypt() {
    const string = this.transfer.serialize(this.cur);
    alert(`Serialized Version: ${string}`);
  }
  decrypt() {
    const string = prompt('Enter to decrypt binary tree');
    if (string === null) return;
    this.emitNode.emit(this.transfer.deserialize(string));
  }
}
