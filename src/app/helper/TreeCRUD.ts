import { UUID } from 'angular2-uuid';
import { Node } from './Node';

export const deleteNodeFromRoot = (root: Node, key: string) => {
  if (root === null || root.key === key) return null;
  root.left = deleteNodeFromRoot(root.left, key);
  root.right = deleteNodeFromRoot(root.right, key);
  return root;
};
export const addNodeFromRoot = (root: Node, curNode: Node) => {
  if (root === null) return null;
  if (root === curNode) {
    if (curNode.left == null) {
      curNode.left = new Node('L', UUID.UUID());
    } else if (curNode.right == null) {
      curNode.right = new Node('R', UUID.UUID());
    }
    return curNode;
  }
  root.left = addNodeFromRoot(root.left, curNode);
  root.right = addNodeFromRoot(root.right, curNode);
  return root;
};
export const editNodeFromRoot = (root: Node, curNode: Node, newVal: string) => {
  if (root === null) return null;
  if (root === curNode) {
    root.val = newVal;
    return root;
  }
  root.left = addNodeFromRoot(root.left, curNode);
  root.right = addNodeFromRoot(root.right, curNode);
  return root;
};
