module Term
  = struct

  open Type
  include Type
  
  type te =
    
    | TeVar: (string * ty) -> te
  
  ;;
  
end
