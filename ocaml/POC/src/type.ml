module Type
  = struct
 
  type typrim =
    
    | Int: typrim
    | Float: typrim

  and tycomp =

    | TyTuple: ty list -> tycomp
    | TyList: ty -> tycomp
  
  and ty =
    
    | TyVar: string -> ty
    | TyPrim: typrim -> ty
    | TyComp: tycomp -> ty
  ;;

  type ty_ctxt = (string, ty) Hashtbl.t;;
  
end
