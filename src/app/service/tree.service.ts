import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Node } from '../helper/Node';
import {
  addNodeFromRoot,
  deleteNodeFromRoot,
  editNodeFromRoot,
} from '../helper/TreeCRUD';

@Injectable({
  providedIn: 'root',
})
export class TreeService {
  private rootSub = new BehaviorSubject<Node>(null);

  setRoot(root: Node) {
    this.rootSub.next(root);
  }
  deleteNode(curNode: Node) {
    let rootNode = this.rootSub.getValue();
    rootNode = deleteNodeFromRoot(rootNode, curNode.key);
    this.setRoot(rootNode);
  }
  addNode(curNode: Node) {
    let rootNode = this.rootSub.getValue();
    rootNode = addNodeFromRoot(rootNode, curNode);
    this.setRoot(rootNode);
  }
  editNode(curNode: Node, newVal: string) {
    let rootNode = this.rootSub.getValue();
    rootNode = editNodeFromRoot(rootNode, curNode, newVal);
    console.log('rootNode', rootNode);
    this.setRoot(rootNode);
  }
  getRoot(): Observable<Node> {
    return this.rootSub.asObservable();
  }
}
