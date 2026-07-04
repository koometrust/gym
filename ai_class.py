murderer(X) :- bagof(Y,contradictsPerson(X,Y),¥s), length(Ys,N), N.
>1

contradictsPerson(A,B) =

claims(A,AClaims), claims(8,BClaims),
contradictsClaims(AClaims,BClaims).

contradictsClaims (Claims, [HIT]) :-
contradictsClaims1(Claims,H); contradictsClaims (Claims).
contradictsClaims1([HIT].C) :-

contradictsClaim(H,C); contradi ctsClaims1(T,C).
contradictsClaim([Claim1Who), [Claim2Who]) :-
contradictory(Claim1,Claim2).

claims{art, [[innocent,art] [knewVic, burt] [knewVic,carl])).
cllsaims{burt, [[outOfTown, burt], [didNotKnowVic,burt]]).
claims(carl, [innocent carl], [inTown,burt], [inTown,carl]]).
contradictory (innocent, murderer).

contradictory (murderer,innocent).
contradictory (outOf Town, inTown).

contradictory inTown,outOfTown).

contradictory (knewVic,didNotKnowVic).

contradictory (didNotKnowVic,knewVic). meaning of each line
