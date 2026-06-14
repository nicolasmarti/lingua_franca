module Test = struct

  type _ tterm =
    | TInt : int -> int tterm
    | TAdd : (int -> int -> int) tterm
    | TApp : ('b -> 'a) tterm * 'b tterm -> 'a tterm
  ;;

  let rec eval : type a. a tterm -> a = function
    | TInt n    -> n                 (* a = int *)
    | TAdd      -> (fun x y -> x+y)  (* a = int -> int -> int *)
    | TApp(f,x) -> (eval f) (eval x)
  
end

