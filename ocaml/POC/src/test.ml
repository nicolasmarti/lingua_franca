module Test = struct

  type _ tterm =
    | TInt : int -> int tterm
    | TAdd : (int -> int -> int) tterm
    | TApp : ('b -> 'a) tterm * 'b tterm -> 'a tterm
  ;;

end
