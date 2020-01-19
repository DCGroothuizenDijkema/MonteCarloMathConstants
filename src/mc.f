
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//
!                                                                                                                                       //
! frog.cpp                                                                                                                              //
!                                                                                                                                       //
! D. C. Groothuizen Dijkema - January, 2020                                                                                             //
!+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+//

! Approximating mathematical constants with Monte Carlo methods

module monte_carlo
  implicit none
contains

  function simulate_e(random_nums,ind) result(cnt)
    real(kind=8), dimension(:), intent(in) :: random_nums
    integer, intent(inout) :: ind
    integer :: cnt

  end function simulate_e

  subroutine approximate_e(n_itr,means)
    !DEC$ ATTRIBUTES DLLEXPORT :: approximate_e
    !DEC$ ATTRIBUTES C :: approximate_e
    implicit none
    integer, intent(in) :: n_itr
    real(kind=8), intent(inout), dimension(n_itr) :: means
    
  end subroutine approximate_e

end module monte_carlo
